#!/usr/bin/env bats

@test "convert 1m to b to strong" {
    result="$(echo -e "convert 1m \033[1mto b to\033[0m strong" | ansifilter --bbcode | inv bbcode-parser-format | pandoc --from=html --to=markdown)"
    expect="$(echo -e "convert\u00a01m\u00a0**to\u00a0b\u00a0to**\u00a0strong\\")"
    [ "$result" == "$expect" ]
}

@test "convert 3m to i to em" {
    result="$(echo -e "convert 3m \033[3mto i to\033[0m em" | ansifilter --bbcode | inv bbcode-parser-format | pandoc --from=html --to=markdown)"
    expect="$(echo -e "convert\u00a03m\u00a0*to\u00a0i\u00a0to*\u00a0em\\")"
    [ "$result" == "$expect" ]
}

@test "convert 4m to u to em" {
    result="$(echo -e "convert 4m \033[4mto u to\033[0m em" | ansifilter --bbcode | inv bbcode-parser-format | pandoc --from=html --to=markdown)"
    expect="$(echo -e "convert\u00a04m\u00a0*to\u00a0u\u00a0to*\u00a0em\\")"
    [ "$result" == "$expect" ]
}