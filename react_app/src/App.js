import React from 'react';
import './App.css';
import {BrowserRouter as Router,Switch,Route} from "react-router-dom";

import Login_page from "./components/Login_page.js";
import Gestion_mdp from "./components/Gestion_mdp.js";
import Verif_mail from "./components/Verif_mail.js";
import Page_principale from "./components/page_principale.js";

class App extends React.Component {
constructor(){
	super()
}

render() {
		return(
			 <Router>
				<Switch>
					<Route exact path="/"> <Login_page /> </Route>
					<Route exact path="/gestion_mdp"> <Gestion_mdp /> </Route>
					<Route exact path="/verif_mail"> <Verif_mail /> </Route>
					<Route exact path="/page_principale"> <Page_principale /> </Route>
				</Switch>
			</Router>
		)
	}
}

export default App;