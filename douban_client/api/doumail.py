# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Doumail(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI Doumail>'

    def get(self, id):
        return self._get('/v2/doumail/%s'%id)

    @property
    def inbox(self):
        return self._get('/v2/doumail/inbox')

    @property
    def outbox(self):
        return self._get('/v2/doumail/outbox')
   
    @property
    def unread(self):
        return self._get('/v2/doumail/inbox/unread')

    def read(self, id):
        return self._put('/v2/doumail/%s'%id)

    def read_by_ids(self, ids):
        return self._put('/v2/doumail/read', ids=ids)

    def delete(self, id):
        return self._delete('/v2/doumail/%s'%id)

    def delete_by_ids(self, ids):
        return self._post('/v2/doumail/delete', ids=ids)

    def new(self, title, content, receiver_id, captcha_token=None, captcha_string=None):
        return self._post('/v2/doumails', title=title, content=content, receiver_id=receiver_id, 
                captcha_toke=captcha_token, captcha_string=captcha_string)