mkdir build && cd build
../configure
# Build and install the Chrome version
make chrome-build
sudo make chrome-install
# You may need to update the linker's cache to find libcurl-impersonate
sudo ldconfig
# Optionally remove all the build files
cd ../ && rm -Rf build