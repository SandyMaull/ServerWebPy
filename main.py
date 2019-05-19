try:
    import trigger
    import sys

    print(22*"=")
    print("\t Kelompok 2")
    print("\t   HTTP")
    print(22*"=")
    print("Please Input an Method u want to use BaseHTTPServer(1) / FLASK( 02 - Still on development! ))")
    Method = input()
    if Method in ['Flask','flask','2','02','Flask(02)','Flask(2)','FLASK']:
        print("This Method is still under development!")
        sys.exit(0)
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

    if Method in ['BaseHTTPServer(1)','BaseHTTPServer','baseHTTPServer','basehttpServer','basehttpserver','1','01']:
        print("Please Input an PORT u want to use")
        PORT = input("PORT: ")

        print("Running a Service Now on port "+PORT+" ... \n")

        trigger.callserver(int(PORT),'localhost')

    else:
        print("Please Input a Correct Statement!")
        sys.exit(0)



except ModuleNotFoundError:
    print("Error while importing a libraries, please make sure u have python3.x and flask!")
    sys.exit(0)
except KeyboardInterrupt:
    print("Service Stop! Goodbye :)")
    sys.exit(0)
except:
    print("Something error with the code :( , please check your coding")
    sys.exit(0)