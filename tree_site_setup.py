from tree_sitter import Language, Parser

Language.build_library(
    # Store the library in the `build` directory
    "build/my-languages.so",
    # Include one or more languages
    ["tree-sitter-java",],
)

JAVA_LANGUAGE = Language("build/my-languages.so", "java")

parser = Parser()
parser.set_language(JAVA_LANGUAGE)

tree = parser.parse(
    bytes(
        """
public String getName() {
    return "Hello";
}
""",
        "utf8",
    )
)

root_node = tree.root_node
print(root_node)