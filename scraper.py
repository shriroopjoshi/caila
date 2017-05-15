import json
import csv
import urllib2

class Course:
    """Container for course information"""
    
    def __init__(self):
        """Initiate all fields to a blank string"""
        self.title = ''
        self.desc = '';
        self.course_number = ''
        self.duration = ''
        self.difficulty = ''
        self.instructors = ''
        self.url = ''
        
    def getaslist(self):
        """Returns the fields as a list"""
        l = []
        l.append(self.title.strip().encode('utf-8'))
        l.append(self.desc.strip().encode('utf-8'));
        l.append(self.course_number.strip().encode('utf-8'))
        l.append(self.duration.strip().encode('utf-8'))
        l.append(self.difficulty.strip().encode('utf-8'))
        l.append(self.instructors.strip().encode('utf-8'))
        l.append(self.url.strip().encode('utf-8'))
        return l
        
    def __str__(self):
        return self.title.strip().encode('utf-8') + ',' + self.desc.strip().encode('utf-8')
    
    def __repr__(self):
        return self.__str__()
    
def scrape(url, filename):
    """Gets the data from given URL and writes it in the given file"""
    courselist = []
    headers = ['title', 'description', 'course number', 'duration', 'difficulty', 'instructors', 'course url']
    with open(filename, 'wb') as outfile:
        wr = csv.writer(outfile)
        wr.writerow(headers)
    courses = json.load(urllib2.urlopen(url))
    for course in courses['courses']:
        c = Course()
        c.title = course['title']
        c.desc = course['summary']
        c.course_number = course['key']
        c.duration = str(course['expected_duration']) + ' ' + str(course['expected_duration_unit'])
        c.difficulty = course['level']
        c.url = 'https://www.udacity.com/course/' + course['slug']
        l = len(course['instructors'])
        for i in xrange(l):
                if(i == 0):
                    c.instructors += course['instructors'][i]['name']
                else:
                    c.instructors += ';' + course['instructors'][i]['name']
        with open(filename, 'ab') as outfile:
            wr = csv.writer(outfile)
            wr.writerow(c.getaslist())


if __name__ == "__main__":
    url = "https://www.udacity.com/public-api/v0/courses"
    filename = 'courses.csv'
    scrape(url, filename)