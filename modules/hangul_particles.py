def kor_particle(word:str,jongseong_particle:str,non_jongseong_particle:str):
    last=word[-1]
    if '가'<=last<='힣':
        if (ord(word[-1])-44032)%28!=0:
            return word+jongseong_particle
        else:
            return word+non_jongseong_particle
    elif last.isdigit():
        if last in '013678':
            return word+jongseong_particle
        else:
            return word+non_jongseong_particle
    else:
        return word+jongseong_particle+'('+non_jongseong_particle+')'