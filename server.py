from app.controllers import *

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
    print('Server started...')