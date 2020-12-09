#!/usr/bin/env bats

@test "convert 1m to b to strong" {
    result="$(echo -e "convert 1m \033[1mto b to\033[0m strong" | ansifilter --bbcode | inv bbcode-parser-format)"
    [ "$result" == "convert&nbsp;1m&nbsp;<strong>to&nbsp;b&nbsp;to</strong>&nbsp;strong<br />" ]
}

@test "convert 3m to i to em" {
    result="$(echo -e "convert 3m \033[3mto i to\033[0m em" | ansifilter --bbcode | inv bbcode-parser-format)"
    [ "$result" == "convert&nbsp;3m&nbsp;<em>to&nbsp;i&nbsp;to</em>&nbsp;em<br />" ]
}

@test "convert 4m to u to strong" {
    result="$(echo -e "convert 4m \033[4mto u to\033[0m strong" | ansifilter --bbcode | inv bbcode-parser-format)"
    [ "$result" == "convert&nbsp;4m&nbsp;<strong>to&nbsp;u&nbsp;to</strong>&nbsp;strong<br />" ]
}