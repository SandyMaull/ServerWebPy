try:
    import sys
    import time
    from http.server import HTTPServer
    from server import Server
    looping = True

    while looping:
        print(4*"\t"+22*"=")
        print(4*"\t"+"  Simple Web Server")
        print(4*"\t"+"\t   HTTP")
        print(4*"\t"+22*"=")
        print("Please Input an Method u want to use")
        Method = input("BaseHTTPServer(1) / FLASK(02 - Still on development!): ")
        if Method in ['Flask','flask','2','02','Flask(02)','Flask(2)','FLASK']:
            print("This Method is still under development!")
            time.sleep(2)

        #     IP = input("IP: ")
        #     PORT = input("PORT: ")
        #
        #
        #     def Framework(IP, PORT):
        #         # try:
        #         app = Flask(__name__)
        #
        #         @app.route("/")
        #         def index():
        #             return redirect("http://localhost/kuronekosan/", code=302)
        #
        #         route = ("/kuronekosan/")
        #
        #         @app.route(route)
        #         def kuronekosan():
        #             file = route + "index.html"
        #             return render_template(file)

                # if __name__ == "__main__":
                #     app.run(debug=False, host=IP, port=PORT)
            #
            # print("Running a Service Now ... \n")
            # Framework(IP,PORT)

        elif Method in ['BaseHTTPServer(1)','BaseHTTPServer','baseHTTPServer','basehttpServer','basehttpserver','1','01']:
            looping = False
            print("Please Input an PORT u want to use")
            PORT = input("PORT: ")
            HOST_NAME = 'localhost'
            PORT_NUMBER = int(PORT)
            httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
            try:
                print(time.asctime(), 'Server Start on - %s:%s' % (HOST_NAME, PORT_NUMBER))
                print("\nCTRL + C to Close Server")
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("Service Stop! Goodbye :)")
                time.sleep(1)
                sys.exit(0)

        else:
            print("Please Input a Correct Statement!")
            time.sleep(1)



except ModuleNotFoundError:
    print("Error while importing a libraries, please make sure u have python3.x and flask!")
    time.sleep(2)
    sys.exit(0)

# except KeyboardInterrupt:
#     print("\nAborting program!! ...")
#     time.sleep(1)
#     sys.exit(0)

# except:
#     print("Something Error with the code :(, please check coding! ...")
#     time.sleep(1)
#     sys.exit(0)