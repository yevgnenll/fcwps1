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

def searchComment(board_id):
    """
    첫 번째 댓글을 달때
    :param board_id: 글번호
    :return:
    """
    maxStart,maxEnd = 0
    for comment in comments:
        if comment['board'] == board_id:
            maxStart = max(maxStart, comment['start'])
            maxEnd = max(maxEnd, comment['end'])



def write_comment():
    board_id = int(input('글 번호: '))
    start = 0
    for article in board:
        if article['id'] == board_id:
            start = article['start']
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
        'start': start+1,
        'end': start+2
    })


def write_comment2(board_id):
    comment_id = int(input('댓글 번호: '))
    text = input('댓글: ')
    info['comment'] += 1
    comments.append({
        'id' : info['comment'],
        'text':text,
        'board':board_id,
        'parent':comment_id
    })

def preorder(parent, depth):
    depth += 1
    for reply in comments:
        if reply['parent'] == parent:
            print('%s %d. %s'%(" "*depth, reply['id'], reply['text']))
            preorder(reply['id'], depth)
            # print("test, comment_id",reply['id'],"parent", reply['parent'])

def show_article():
    board_id = int(input('글 번호: '))
    depth = 1
    if type(board_id) is not type(1):
        print("다시해")
        return
    for article in board:
        if article['id'] == board_id:
            print('%d. %s'%(article['id'],article['text']))
            break
    else:
        print('글 없음')
        return
    for comment in comments:
        if comment['board'] == board_id and comment['parent'] == 0:
            print('%s %d. %s'%(" ", comment['id'],comment['text']))
            preorder(comment['id'], depth)
            # 해당 코멘드의 id가 depth2의 parent가 된다

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
