# Bookstore with protected React JS

- This is full stack project
	- The backend is python django.
	- The frontend is react redux.

- To download it, clone : [https://github.com/ccapeng/bookstore_pro.git](https://github.com/ccapeng/bookstore_pro.git)

- To start backend,
	- Make sure `python` and `pip` installed.
	- Then cd to `bookstore_pro` directory.
	- For the first time, create virtual environment  
		`python -m venv env`
	- Then start the virtual environment `.\env\Scripts\activate`
	- Also for the very first time, run `pip install -r requirements.txt`
	- To start server, run `python manage.py runserver`
	- Open browser in URL [http://localhost:8000](http://localhost:8000)  
		The login/password is `admin/admin123`
	
- To start frontend,
	- Make sure `npm` installed.
	- Run `npm install` to install all react dependency modules.
	- To deploy react js, run `npm run dev`. See package.json for the deployment.
	- The react js file is deployed to `frontend/js/main.js`.  
		In this case, the main.js is not exposed to public and only available after login.
		
