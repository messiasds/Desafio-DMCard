import React from 'react'
import Titulo from '../components/Titulo'
import axios from 'axios'
import { Link } from 'react-router-dom'


class SolicitacaoCartaoForm extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            //dados: {
                nome:"",
                data_nascimento:"",
                rg:"",
                cpf:"",
                telefone:"",
                email:"",
                renda:"",
            //},
            //path_detalhes:"/lista",
            //salvo_flah:false
        }

        this.handleInputChange = this.handleInputChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    handleInputChange(event){
        const target = event.target
        const value =  target.value
        const name = target.name

        this.setState({
             [name] : value
        })
    }
    
    handleSubmit(event){
        event.preventDefault();
        console.log(this.state);
        let resp;
        resp = this.salvarDados();
        console.log(resp);
        
    }

    salvarDados(){

        let url = 'http://127.0.0.1:9090/solicitacoes'
        axios.post(url, this.state)
            .then((response) => {
                alert("salvo com sucesso");

            })
    }

    render(){
        return (
            <form onSubmit={this.handleSubmit} >
                nome
                <input name="nome" type="text" value={this.state.nome} onChange={this.handleInputChange}/><br />
                rg
                <input name="rg" type="text" value={this.state.rg } onChange={this.handleInputChange}/><br />
                cpf
                <input name="cpf" type="text" value={this.state.cpf } onChange={this.handleInputChange}/><br />
                nascimento
                <input name="data_nascimento" type="date" value={this.state.nascimento} onChange={this.handleInputChange} /><br/>
                telefone
                <input name="telefone" type="text" value={this.state.telefone } onChange={this.handleInputChange}/><br />
                renda
                <input name="renda" type="text" value={this.state.renda } onChange={this.handleInputChange}/><br />
                email
                <input name="email" type="text" value={this.state.email } onChange={this.handleInputChange}/><br />
                <input type="submit" value="Salvar" />
            </form>
        )
    }

}


export default () =>  (
    <>
    <Titulo titulo = 'Pedir cartão' />
    <SolicitacaoCartaoForm />
    </>
)