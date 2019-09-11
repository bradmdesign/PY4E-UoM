import cv2
import curses
import configparser
import time

# read the config file
config = configparser.ConfigParser()
config.read('tcconf.ini')
zoom = int(config['DEFAULT']['Zoom'])
invert = bool(config['DEFAULT']['Invert'])
refresh = float(int(config['DEFAULT']['Refresh'])/100)
camsize = int(config["DEFAULT"]["CameraSize"])
c_input = int(config["DEFAULT"]["Input"])

# set up curses
stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.keypad(1)
stdscr.nodelay(1)
term_h, term_w = stdscr.getmaxyx()

# set up camera
c_size = round(camsize/zoom)
win = cv2.VideoCapture(c_input)
ret = win.set(3, c_size), win.set(4, c_size)
step_x = c_size / term_w
step_y = c_size / term_h


if invert:
    ascii_values = {
        50: '%',
        75: '#',
        100: '*',
        125: '+',
        150: '-',
        175: ':',
        210: '.',
        255: ' ',
    }
else:
    ascii_values = {
        50: ' ',
        75: '.',
        100: ':',
        125: '-',
        150: '+',
        175: '*',
        210: '#',
        255: '%',
    }


def xrange(n):
    return range(int(n * step_x), int((n+1) * step_x))


def yrange(n):
    return range(int(n * step_y), int((n+1) * step_y))


def to_ascii(n):
    n = n
    while 1:
        try:
            a = ascii_values[n]
            return a
        except KeyError:
            n += 1


def main():
    while 1:
        ret, frame = win.read()
        M = cv2.getRotationMatrix2D((c_size / 2, c_size / 2), 90, 1)
        frame = cv2.warpAffine(frame, M, (c_size, c_size))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        for x in range(term_w - 1):
            for y in range(term_h):
                avg = 0
                pts = 0
                for i in xrange(x):
                    for j in yrange(y):
                        avg += gray[i, j]
                        pts += 1
                stdscr.addch(y, x, to_ascii(round(avg / pts)))

        c = stdscr.getch()
        if c == ord('q'):
            break
        stdscr.refresh()
        time.sleep(refresh)


if __name__ == "__main__":
    main()
    cv2.destroyAllWindows()
    win.release()
    curses.nocbreak()
    stdscr.keypad(0)
    stdscr.nodelay(0)
    curses.echo()
    curses.endwin()
