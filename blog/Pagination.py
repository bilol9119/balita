class Pagination:
    def __init__(self, blogs, num):
        self.currpage = 1
        self.ans = []
        blogs = list(blogs)
        n = len(blogs)
        while n - num >= 0:
            box = []
            for i in range(num):
                blog = blogs.pop(0)
                box.append(blog)
            self.ans.append(tuple(box))
            n -= num
        if n > 0:
            self.ans.append(tuple(blogs))

    def get_page(self, page):
        if len(self.ans) >= int(page):
            self.currpage = int(page)
            return self.ans[int(page)-1]
        return []

    def has_previous(self):
        if self.currpage - 1 >= 1:
            return True
        return False

    def previous(self):
        return self.currpage-1

    def page_range(self):
        page = range(1, len(self.ans)+1)
        return page

    def object_list(self):
        return self.ans

    def curr_page(self):
        return self.currpage

    def has_next(self):
        if self.currpage + 1 <= len(self.ans):
            return True
        return False

    def next(self):
        return self.currpage + 1