import React, { Component } from 'react'
import axios from 'axios'

export default class Tabela extends Component {

    state = {
      lista_li: []
    };

    componentDidMount(){

        this.get_dados()
    }

    montar_lista(dados){

        // cria um novo array contendo uma lista de <LI> com os dados do JSON

        let linhas = dados.map((linha) =>
            <li> { linha.nome }  - { linha.credito } - {linha.cartao_aprovado.toString() } </li>
         )
         this.setState({lista_li:linhas})
    }

    get_dados(){

        let url = 'http://127.0.0.1:9090/solicitacoes'
        axios.get(url)
            .then((response) => {
                let dados = JSON.parse(JSON.stringify(response.data))
                this.montar_lista(dados)
            })

    }

    render(){
        return (
            <>
            <ul> 
                { this.state.lista_li }
            </ul>
            </>
        )
    }
}


