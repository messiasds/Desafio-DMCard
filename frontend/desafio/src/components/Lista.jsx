import React, { Component } from 'react'
import axios from 'axios'
import ListItem from '@material-ui/core/ListItem';
import List from '@material-ui/core/List';
import {ListItemText, ListItemAvatar, Avatar} from '@material-ui/core';
import {Link} from 'react-router-dom'

export default class Tabela extends Component {

    state = {
      lista_li: []
    };

    componentDidMount(){

        this.get_dados()
    }

    verificar_cartao_aprovado(){
        return null

    }

    montar_lista(dados){

        // cria um novo array contendo uma lista de <LI> com os dados do JSON

        let linhas = dados.map((linha) => 
            
            <ListItem button divider component={Link} to={
                {
                    pathname:"/detalhes",
                    state: linha
                }
            }>
                <ListItemAvatar>
                    { linha.cartao_aprovado
                      ? <Avatar  alt="Remy Sharp" src="https://media.istockphoto.com/vectors/check-mark-vector-tick-green-icon-in-circle-approved-symbol-checkmark-vector-id1261448792" />
                      : <Avatar  alt="Remy Sharp" src="https://png.pngtree.com/png-vector/20190618/ourlarge/pngtree-true-and-false-symbols-accept-rejected-for-evaluation-vector-simple-png-image_1502129.jpg" />
                    }
                </ListItemAvatar>
                <ListItemText >
                { linha.nome }  - R$ { linha.credito } {/*linha.cartao_aprovado.toString() */} 
                </ListItemText>
            </ListItem >
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
            <List >
                { this.state.lista_li}
            </List>
            </>

        )
    }
}


