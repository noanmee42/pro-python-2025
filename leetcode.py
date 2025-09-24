x = int(input());
safe_x = x;
cnt = 0;
bool = True;

while safe_x != 0:
    safe_x //= 10;
    cnt += 1;
def to_back(x):
    return(x[::-1]);
x_viceversa_array = to_back(str(x));
for i in range(cnt):
    x_array = list(map(int, str(x)));
    if int(x_array[i]) == int(x_viceversa_array[i]):
        continue;
    else:
        bool = False;
        break;
print(bool);
