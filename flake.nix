# this config is reliant on cachix to avoid compiling the cuda packages
# install cachix and do cachix use nix-community and dont forget to import it in your configuration.nix
# Ultralytics sometimes doesn't find the dataset images because it has a different path by default. To fix this just
# go to .config/Ultralytics/settings.json and change the path by removing the datasets directory
{
  description = "VR Headset Filter Development Environment";

  nixConfig = {
    extra-substituters = [
      "https://nix-community.cachix.org"
      "https://vrheadcache.cachix.org"
    ];
    extra-trusted-public-keys = [
      "nix-community.cachix.org-1:mB9FSh9qf2dCimDSUo8Zy7bkq5CX+/rkCWyvRCYg3Fs="
      "vrheadcache.cachix.org-1:v0XsYmHf9iA9ZtIsdc+Bjyqtzx6DO5f/fiXq2Lq+blA="
    ];
  };

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {
        inherit system;
        config = {
          allowUnfree = true;
          # cudaSupport = true;
        };
      };

      python = pkgs.python312;

      pythonWithPackages = python.withPackages (ps:
        with ps; [
          numpy
          pillow
          pip

          torch-bin
          torchvision-bin

          pydantic

          requests
          # fastapi
          # fastapi-cli

          opencv4

          # for ultralytics
          tqdm
        ]);
    in {
      devShells.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          python312Packages.python-lsp-server
          black
          pythonWithPackages

          # For CUDA support if you already have it remove these two lines
          cudaPackages.cudatoolkit
          cudaPackages.cudnn

          pkg-config
          # ffmpeg

          sqlite

          gtk2.dev
          libGL.dev
        ];

        shellHook = ''
          export CUDA_PATH=${pkgs.cudatoolkit}
          export LD_LIBRARY_PATH=${pkgs.cudatoolkit}/lib:$LD_LIBRARY_PATH
          export EXTRA_CCFLAGS="-I/usr/include"

          if [ ! -d .venv ]; then
            echo "Creating virtualenv with ultralytics ..."
            ${python.interpreter} -m venv .venv
            source .venv/bin/activate
            pip install --upgrade pip
            pip install ultralytics pytest fastapi mistralai
             pip install "fastapi[standard]"
          else
            source .venv/bin/activate
          fi

          echo "Virtualenv activated. 'ultralytics' installed with."
        '';
      };
    });
}
