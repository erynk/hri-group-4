//Import express.js module and create its variable.
const express=require('express');
const app=express();

app.set('view engine', 'ejs');

// middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

//Import PythonShell module.
const {PythonShell} = require('python-shell');

//Router to handle the incoming request.
app.get("/", (req, res, next)=>{

	//the schedule array
	let schedule = [];

	const events = new Array;
	const eventsHours = new Array;
	const eventsMinutes = new Array;

	//Here are the option object in which arguments can be passed for the python_test.js.
	let options = {
		mode: 'text',
		pythonPath: 'python2',
		pythonOptions: ['-u'], // get print results in real-time
	};
	
	PythonShell.run('read-schedule.py', options, function (err, result){
		if (err) throw err;
		schedule = [];
		// result is an array consisting of messages collected
		//during execution of script.
		schedule = result.toString();
		schedule = schedule.replace('[[', '');
		schedule = schedule.replace(']]','');
		schedule = schedule.split(',');

		// trim inputs 

		for (let i = 0; i < schedule.length; i++) {
			schedule[i] = schedule[i].replace(/["']/g, '');
			schedule[i] = schedule[i].trim();
			if (i % 3 == 0) {
				events.push(schedule[i]);
			}
			
			else if ( (i + 2) % 3 == 0) {
				eventsHours.push(schedule[i]);
			}
			else if ( (i + 1) % 3 == 0) {
				eventsMinutes.push(schedule[i])
			}
		}

		console.log(events);
	
		res.render("index", { events:events, eventsHours:eventsHours, eventsMinutes:eventsMinutes });
	});
});

// POST method route
app.post('/', (req, res) => {

	let updatedSchedule = Object.values(req.body);
	let events = [];
	let eventsHours = [];
	let eventsMinutes = [];

	
	//Here are the option object in which arguments can be passed for the python_test.js.
	let options = {
		mode: 'text',
		pythonPath: 'python2',
		pythonOptions: ['-u'], // get print results in real-time
		args: [updatedSchedule],
	};
		
	PythonShell.run('write-schedule.py', options, function (err, result){
		if (err) throw err;
		console.log(updatedSchedule);

		for (let i = 0; i < updatedSchedule.length; i++) {
			if (i % 3 == 0) {
				events.push(updatedSchedule[i]);
			}
			
			else if ( (i + 2) % 3 == 0) {
				eventsHours.push(updatedSchedule[i]);
			}
			else if ( (i + 1) % 3 == 0) {
				eventsMinutes.push(updatedSchedule[i])
			}
		}

		res.redirect("/");
	});

});

//Creates the server on default port 8000 and can be accessed through localhost:8000
const port=8000;
app.listen(port, ()=>console.log(`Server connected to ${port}`));
