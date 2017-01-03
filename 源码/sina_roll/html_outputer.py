# coding:utf8


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        for data in self.datas:
            fout = open('output.html','a')
            fout.write("Title: %s" % data['title'])
            print type(data['title'])
            fout.write('\n')
            fout.write("Summary: %s" % data['summary'])
            fout.write('\n')
        print 'output success'
#    def output_html(self):
#        fout = open('output.html', 'a')
#        fout.write("<!DOCTYPE html>")
#        fout.write("<html>")
#        # fout.write("<meta charset='utf-8'>")
#        # fout.write("<meta charset='gbk'>")
#        fout.write("<body>")
#        fout.write("<table>")
#
#        # ASCII
#        for data in self.datas:
#            fout.write("<tr>")
#            #fout.write("<td>%s</td>" % data['url'].encode('utf-8'))
#            #fout.write("<td>%s</td>" % data['title'].encode('utf-8')
#            #fout.write("<td>%s</td>" % data['summary'].encode('utf-8')
#            fout.write("</tr>")
#
#        fout.write("</table>")
#        fout.write("</body>")
#        fout.write("</html>")
