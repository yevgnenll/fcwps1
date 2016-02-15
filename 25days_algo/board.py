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
            info['board'] -=1
            break
    while True:
        for i in range(len(comments)):
            if comments[i]['board'] == board_id:
                del comments[i]
                info['comment'] -= 1
                break
        break

def write_comment():
    board_id = int(input('글 번호: '))
    comment = input('댓글 내용: ')
    # 글이 있는지 확인
    info['comment'] += 1
    comments.append({
        'id': info['comment'],
        'text': comment,
        'board': board_id
    })

def show_article():
    board_id = int(input('글 번호: '))
    isComment = False
    for article in board:
        if article['id'] == board_id:
            print('%d. %s'%(article['id'],article['text']))
            break
    else:
        print('글 없음')
        return

    for reply in comments:
        if reply['board'] == board_id:
            print('    [re:] %s' %(reply['text']))


while True:
    cmd = input('글 쓰기(w), 종료(q), 목록(l), 삭제(d), 댓글(c), 읽기(r): ')
    if cmd == 'q':
        break
    if cmd == 'w':
        text = input('글 내용: ')
        info['board']  += 1
        board.append({
            'id' : info['board'],
            'text': text
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
