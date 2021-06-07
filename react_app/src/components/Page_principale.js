import React from 'react';
import {Redirect} from 'react-router-dom';
import axios from 'axios';

import {Button, Card, Form} from 'react-bootstrap'

import ElementConversation from "./ElementConversation.js";
import ElementMessage from "./ElementMessage.js";
import PageModalAjouter from "./PageModalAjouter.js";
import PageModalAjouterUser from "./PageModalAjouterUser.js";

class PagePrincipale extends React.Component {
	constructor(){
		super()

		let logged_temp
		if (localStorage.getItem("logged") === null) {logged_temp = false}
		else {logged_temp = localStorage.getItem("logged")}

		this.state = {
			logged: logged_temp,
			conversations:[],
			conversation_a_visualiser:-1,
			messages:[],
			texte:""
		}
		this.changerVisualiser = this.changerVisualiser.bind(this)
		this.fonction_pour_re_render = this.fonction_pour_re_render.bind(this)
		this.envoyerHandler = this.envoyerHandler.bind(this)
		this.quitterHandler = this.quitterHandler.bind(this)
		this.deconnexionHandler = this.deconnexionHandler.bind(this)
	}

	componentDidMount(){
        axios.post('http://127.0.0.1:1161/principal5',{token:localStorage.getItem("token")})
            .then(response => {
                if(response.status === 200){
                    if (response.data.retour === "ok"){
                        this.setState({"conversations":response.data.valeurs})
                                                      }
                                           }
                              }
                  ).catch(error => {console.log(error)})
        if (this.state.conversation_a_visualiser !== -1){
	        axios.post('http://127.0.0.1:1161/principal6',{token:localStorage.getItem("token"),ref_conv:this.state.conversation_a_visualiser })
	            .then(response => {
	                if(response.status === 200){
	                    if (response.data.retour === "ok"){
	                        this.setState({"messages":response.data.valeurs})
	                                                      }
	                                           }
	                              }
	                  ).catch(error => {console.log(error)})
        }
	}

	fonction_pour_re_render(){
        axios.post('http://127.0.0.1:1161/principal5',{token:localStorage.getItem("token")})
            .then(response => {
                if(response.status === 200){
                    if (response.data.retour === "ok"){
                        this.setState({"conversations":response.data.valeurs})
                                                      }
                                           }
                              }
                  ).catch(error => {console.log(error)})
        if (this.state.conversation_a_visualiser !== -1){
	        axios.post('http://127.0.0.1:1161/principal6',{token:localStorage.getItem("token"),ref_conv:this.state.conversation_a_visualiser })
	            .then(response => {
	                if(response.status === 200){
	                    if (response.data.retour === "ok"){
	                        this.setState({"messages":response.data.valeurs})
	                                                      }
	                                           }
	                              }
	                  ).catch(error => {console.log(error)})
        }
        this.forceUpdate()
	}

	changerVisualiser(arg){
		this.setState({conversation_a_visualiser:arg},() => this.fonction_pour_re_render())
	}

	changeHandler = (e) => {
		this.setState({[e.target.name]: e.target.value})
	}

	envoyerHandler(){
		if (this.state.conversation_a_visualiser !== -1){
	        axios.post('http://127.0.0.1:1161/principal4',{token:localStorage.getItem("token"),ref_conv:this.state.conversation_a_visualiser,message:this.state.texte})
	            .then(response => {
	                if(response.status === 200){
	                    if (response.data.retour === "ok"){
	                        this.setState({texte:""}, () => this.fonction_pour_re_render())
	                                                      }
	                                           }
	                              }
	                  ).catch(error => {console.log(error)})
	    }
	}

	quitterHandler(){
		if (this.state.conversation_a_visualiser !== -1){
	        axios.post('http://127.0.0.1:1161/principal3',{token:localStorage.getItem("token"),ref_conv:this.state.conversation_a_visualiser})
	            .then(response => {
	                if(response.status === 200){
	                    if (response.data.retour === "ok"){
	                        this.setState({texte:"",conversation_a_visualiser:-1,messages:[]}, () => this.fonction_pour_re_render())
	                                                      }
	                                           }
	                              }
	                  ).catch(error => {console.log(error)})
	    }
	}

	deconnexionHandler = (e) => {
		e.preventDefault()
		localStorage.setItem("logged",false)
		this.setState({"logged":false})
		localStorage.removeItem("token")
	}

	render() {
	  	const {logged} = this.state
	    if (logged === false) {return <Redirect to="/" />}

		const {texte} = this.state

		const elements_conversation = this.state.conversations
			.map((elem,i) => <ElementConversation infos={elem} fonction_pour_re_render={this.fonction_pour_re_render} changerVisualiser={this.changerVisualiser}/>)

		const elements_messages = this.state.messages
			.map((elem,i) => <ElementMessage infos={elem} />)

		return(
			<div className="App">
				<div class="aaaaa">
					<div class="aaaab">
						<div class="aaaac">
							<div class="aaaaf">
								<Card bg="dark" text="light"> Conversations </Card>
							</div>
							<div class="aaaag">
								{elements_conversation}
							</div>
							<div>
								<PageModalAjouter fonction_pour_re_render={this.fonction_pour_re_render} />
							</div>
						</div>
						<div class="aaaad">
							<div class="aaaai">
								<Card bg="dark" text="light"> Messages </Card>
							</div>
							<div class="aaaaj">
								{elements_messages}
							</div>
							<div class="aaaak">
								<Form>
								  <Form.Group controlId="formBasicPassword">
								    <Form.Control as="textarea" rows={3} type="text" placeholder="Entrez du texte ..." name="texte" value={texte} onChange={this.changeHandler} />
								  </Form.Group>
								</Form>
							</div>
							<div class="aaaal">
								<Button variant="dark" onClick={this.envoyerHandler}> Envoyer </Button>
							</div>
						</div>
						<div class="aaaae">
							<div class="aaaao">
								<Button variant="dark" onClick={this.deconnexionHandler}> Se déconnecter </Button>
							</div>
							<div>
								<PageModalAjouterUser fonction_pour_re_render={this.fonction_pour_re_render} infos={this.state} />
							</div>
							<div class="aaaan">
								<Button variant="dark" onClick={this.quitterHandler}> Quitter la conversation </Button>
							</div>
						</div>
					</div>
				</div>
			</div>
		)
	}
}

export default PagePrincipale;
