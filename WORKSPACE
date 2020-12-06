workspace(name = "io_bazel_rules_jsonnet")

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

local_repository(
    name = "examples",
    path = "examples",
)

local_repository(
    name = "docs",
    path = "docs",
)

# TODO: Move this to examples/WORKSPACE when recursive repositories are enabled.
load("//canary:canary.bzl", "canary_repositories")

canary_repositories()

git_repository(
    name = "io_bazel_skydoc",
    remote = "https://github.com/bazelbuild/skydoc.git",
    commit = "4ea7b8257d11ac33eef7e9daadbedbfe375d9236", # release 0.2.0
    shallow_since = "1543532884 -0500",
)

load("@io_bazel_skydoc//skylark:skylark.bzl", "skydoc_repositories")

skydoc_repositories()