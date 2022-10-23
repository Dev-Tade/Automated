if ($args[0] -ne "") {
    git add .
    git commit -m $args[0]
}