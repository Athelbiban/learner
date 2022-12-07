# shellcheck disable=SC1073

calc ()
{
  result=$[$arg1 $oper $arg2]
}

reg1='^-?[0-9]+$'
reg2='^[-+*/%]$|^[*]{2}$'
while [ True ]; do
  read arg1 oper arg2
  if [[ $arg1 == "exit" ]]; then
      echo "bye"
      exit
  elif [[ $arg1 =~ $reg1 && $arg2 =~ $reg1 && $oper =~ $reg2 ]]; then
      calc $arg1 $oper $arg2
      echo $result
  else
      echo "error"
      exit
  fi
done
