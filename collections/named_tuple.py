import json
from collections import namedtuple

## 定義
Item = namedtuple('Article', ('title', 'topic', 'body'))

## 生成
item1 = Item('support vector machine', 'ml', '....')
item2 = Item(title='lda', topic='ml', body='...')

## アクセス

print(item1.title)
print(item2.topic)

## JSON にダンプ

print(json.dumps(item1))
