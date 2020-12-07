#!/usr/bin/env bats

@test "convert b to strong" {
    result="$(echo -n "[b]convert b to strong[/b]" | inv bbcode-parser-format)"
    [ "$result" == "<strong>convert b to strong</strong>" ]
}

@test "convert i to em" {
    result="$(echo -n "[i]convert i to em[/i]" | inv bbcode-parser-format)"
    [ "$result" == "<em>convert i to em</em>" ]
}

@test "convert u to strong" {
    result="$(echo -n "[u]convert u to strong[/u]" | inv bbcode-parser-format)"
    [ "$result" == "<strong>convert u to strong</strong>" ]
}