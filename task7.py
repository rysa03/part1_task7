def biggest_guy(f_guy, s_guy, t_guy):
    if f_guy>s_guy and f_guy>t_guy:
        return f_guy
    elif s_guy>f_guy and s_guy>t_guy:
        return s_guy
    else:
        return t_guy

def test_biggest_guy():
    try:
        assert biggest_guy(1, 3, 2) == 3
        assert biggest_guy(30, 10, 20) == 30
        assert biggest_guy(20, 10, 30) == 30
        assert biggest_guy(2, 1, 9) == 9
        assert biggest_guy('a', 'a', 'b') == 'b' # 'b' is greater than 'a'
    except (AssertionError) as e:
        print(e,'Wrong')
#print("Wrong!!")
print("Correct buddy!!!")
test_biggest_guy()