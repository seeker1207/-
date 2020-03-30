def solution(genres, plays):
    answer = []
    dic_play = {}
    dic_num = {}
    tpl_num_play_genre = []
    i = 0
    for genre, play in zip(genres, plays):
        dic_play[genre] = dic_play.get(genre, 0) + play
        dic_num.setdefault(genre, []).append(i)
        i += 1

    dic_play_sorted = sorted(dic_play.items(), key=lambda x: x[1], reverse=True)

    for genre, play in dic_play_sorted:
        for s_num in dic_num[genre]:
            tpl_num_play_genre.append([s_num, plays[s_num]])

        tpl_sorted = sorted(tpl_num_play_genre, key=lambda x: x[0])
        tpl_sorted = sorted(tpl_num_play_genre, key=lambda x: x[1], reverse=True)

        answer.extend([tpl[0] for tpl in tpl_sorted[:2]])
        tpl_num_play_genre = []

    return answer