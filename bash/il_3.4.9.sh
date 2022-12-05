ready="yes"

while [[ -n $ready ]]; do
  read n m
  ready=$n
  while [[ n -ne m ]]; do
    if [[ n -lt m ]]; then
      m=$((m - n))
    else
      n=$((n - m))
    fi
  done
  if [[ -n $ready ]]; then
    echo "GCD is $n"
  else
    echo "bye"
  fi
done
