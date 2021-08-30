from conans import ConanFile, tools, CMake
from conans.tools import check_min_cppstd
import os


class RepackedCorrade(ConanFile):
    name = "repacked_corrade"
    homepage = "https://github.com/werto87/repacked_corrade"
    description = "repacked corrade https://github.com/mosra/corrade.git"
    topics = ("utility", "magnum-dependency")
    license = "BSL-1.0"
    url = "https://gitlab.com/werto87/conan-the-example"
    settings = "compiler"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def configure(self):
        if self.settings.compiler.cppstd:
            check_min_cppstd(self, "20")

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.build()

    def package(self):
        self.copy("*.h*", dst=f"include/{self.name}",
                  src=f"{self._source_subfolder()}/{self.name}")

    def package_info(self):
        self.cpp_info.libs = ["corrade"]
