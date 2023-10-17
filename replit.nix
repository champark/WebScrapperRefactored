{ pkgs }: {
  deps = [
    pkgs.git init
    pkgs.chromium
    pkgs.chromedriver
  ];
}