load("//canary/private:common.bzl", "MINIMUM_BAZEL_VERSION")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:utils.bzl", "maybe")

def canary_rules_dependencies(is_rules_go = False):
    # Repository of standard constraint settings and values.
    # Bazel declares this automatically after 0.28.0, but it's better to
    # define an explicit version.
    archive_name = "platforms"
    if archive_name not in native.existing_rules():
        http_archive(
            name = archive_name,
            strip_prefix = "platforms-0.0.1",
            # 0.0.1, latest as of 2020-12-01
            urls = [
                "https://mirror.bazel.build/github.com/bazelbuild/platforms/archive/0.0.1.zip",
                "https://github.com/bazelbuild/platforms/archive/0.0.1.zip",
            ],
            sha256 = "2bf34f026351d4b4b46b17956aa5b977cc1279d5679385f6885bf574dec5570c",
        )

    # Needed by rules_go implementation and tests.
    # We can't call bazel_skylib_workspace from here. At the moment, it's only
    # used to register unittest toolchains, which rules_go does not need.
    archive_name = "bazel_skylib"
    if archive_name not in native.existing_rules():
        http_archive(
            name = archive_name,
            # 1.0.3, latest as of 2020-12-01
            urls = [
                "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.0.3/bazel-skylib-1.0.3.tar.gz",
                "https://github.com/bazelbuild/bazel-skylib/releases/download/1.0.3/bazel-skylib-1.0.3.tar.gz",
            ],
            sha256 = "1c531376ac7e5a180e0237938a2536de0c54d93f5c278634818e0efc952dd56c",
        )
