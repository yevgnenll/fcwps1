import json
import os

info = {
    'board': 0,
    'comment': 0
}
board = []
comments = []

if os.path.exists('info.json'):
    with open('info.json','r') as fp:
        info = json.loads(fp.read())


if os.path.exists('board.json'):
    with open('board.json','r') as fp:
        board = json.loads(fp.read())

if os.path.exists('comments.json'):
    with open('comments.json','r') as fp:
        comments = json.loads(fp.read())

def show_list():
    for article in board:
        print('%d. %s'%(article['id'],article['text']))

def delete_article():
    board_id = int(input('글 번호: '))
    for i in range(len(board)):
        if board[i]['id'] == board_id:

            del board[i]
            break

def write_comment():
    board_id = int(input('글 번호: '))
    end = 0

    for article in board:
        if article['id'] == board_id:
            end = article['end']
            article['end']+=2
            break
    else:
        print('글 없음')
        return

    comment = input('댓글 내용: ')
    info['comment'] += 1
    comments.append({
        'id': info['comment'],
        'text': comment,
        'board': board_id,
        'start': end,
        'end': end+1,
        'depth': 1
    })


def write_comment2(board_id, start, depth):
    comment_id = int(input('댓글 번호: '))
    depth = 0
    start = 0

    for comment in comments:
        if comment['id'] == comment_id:
            # 여기서 찾아낸 comment에 리플을 달것이다
            depth= comment['depth']
            start = comment['start']
            break
    updateStartEnd(board_id, start)
    text = input('댓글: ')
    info['comment'] += 1
    comments.append({
        'id' : info['comment'],
        'text':text,
        'board':board_id,
        'start': start + 1,
        'end': start+2,
        'depth':depth+1
    })

def updateStartEnd(board_id,start):

    comStartMax=[]
    for comment in comments:
        # 해당 글의 코멘트인 경우에
        if comment['board'] == board_id:
            # 새로운 코멘트가 추가되기 전 모든 start, end의 값을 변경한다
            if comment['start'] > start:
                comment['start'] += 2
                comment['end'] += 2
                comStartMax.append(comment['end'])

            # parent comment의 경우에는 start가 유지되어야 한다
            if comment['start'] == start:
                comment['end'] += 3

    # 원래 글의 end값을 수정한다 +=2
    for aritcle in board:
        if board_id == aritcle['id']:
            aritcle['end'] = max(comStartMax)+2

def show_article():
    board_id = int(input('글 번호: '))
    if type(board_id) is not type(1):
        print("다시해")
        return
    for article in board:
        if article['id'] == board_id:
            print('%d. %s'%(article['id'],article['text']), article['end'])
            break
    else:
        print('글 없음')
        return
    # search all comments
    for comment in comments:
        if comment['board'] == board_id:
            print('%s %d. %s'%(" ", comment['id'],comment['text']), comment['end'])

    cmd = input('닫기(q), 댓글의 댓글 달기(c): ')
    if cmd == 'c':
        write_comment2(board_id)

while True:
    cmd = input('글 쓰기(w), 종료(q), 목록(l), 삭제(d), 댓글(c), 읽기(r): ')
    if cmd == 'q':
        break
    if cmd == 'w':
        text = input('글 내용: ')
        info['board']  += 1
        board.append({
            'id' : info['board'],
            'text': text,
            'start':1,
            'end': 2,
            'depth':0
        })
    elif cmd == 'l':
        show_list()
    elif cmd == 'd':
        delete_article()
    elif cmd == 'c':
        write_comment()
    elif cmd == 'r':
        show_article()

with open('board.json','w') as fp:
    fp.write(json.dumps(board))
with open('comments.json','w') as fp:
    fp.write(json.dumps(comments))
with open('info.json','w') as fp:
    fp.write(json.dumps(info))
