from conans import ConanFile, CMake, tools


class CpprestsdkConan(ConanFile):
    name = "using-shared-lib-conan"
    version = "1.0.0"
    license = "MIT"
    author = "Nasim Kabiliravi <conanrepos@gmail.com>"
    url = "https://github.com/mycpptutorial/using-shared-lib-conan"
    description = "A C++ sample to learn how to use a shared library created a conan package."
    topics = ("Shared Library", "Using Shared Library", "Using Shared Library with Conan", "conan", "C++", "cpp", "C++ tutorial")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports = "*"

    def requirements(self):
        self.requires("datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.build()

    def package(self):
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["using-shared-lib-conan"]
