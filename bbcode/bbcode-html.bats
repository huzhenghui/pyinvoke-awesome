#!/usr/bin/env bats

@test "convert b to strong" {
    result="$(echo -n "[b]convert b to strong[/b]" | inv bbcode-parser-format)"
    [ "$result" == "<strong>convert&nbsp;b&nbsp;to&nbsp;strong</strong>" ]
}

@test "convert i to em" {
    result="$(echo -n "[i]convert i to em[/i]" | inv bbcode-parser-format)"
    [ "$result" == "<em>convert&nbsp;i&nbsp;to&nbsp;em</em>" ]
}

@test "convert u to em" {
    result="$(echo -n "[u]convert u to em[/u]" | inv bbcode-parser-format)"
    [ "$result" == "<em>convert&nbsp;u&nbsp;to&nbsp;em</em>" ]
}