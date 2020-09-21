import React, { Component } from 'react'
import Titulo from '../components/Titulo'
import axios from 'axios'
import {Button, Box, Container} from '@material-ui/core'
import {Link} from 'react-router-dom'

export default class SolicitacaoDetalhes extends Component {
    constructor(props){
        super(props)
        this.state = {
            dados: props.location.state
        }
        this.excluir = this.excluir.bind(this)

    }

    excluir() {
        
        axios.delete('http://127.0.0.1:9090/solicitacoes/'+this.state.dados.id)
        .then((response) => {
            alert("Excluído com sucesso!");

        })
    }

    render(){
        return (
          <>
            <Container maxWidth='sm'>
            <Titulo titulo = 'Detalhes' />
            <h2> Dados Pessoais </h2>
            <p>Nome: {this.state.dados.nome} </p> 
            <p>telefone: {this.state.dados.telefone} </p> 
            <p>email: {this.state.dados.email} </p> 
            <p>renda: {this.state.dados.renda} </p> 
            <p>data nascimento: {this.state.dados.data_nascimento} </p> 
            <h2> Dados do cartao </h2>
            <h4> {this.state.dados.cartao_aprovado
                   ? "CARTÃO APROVADO"
                   : "CARTÃO NÃO APROVADO!" 
                  }
            </h4>
            <p>Score: {this.state.dados.pontuacao} </p> 
            <p>Credito: R$ {this.state.dados.credito} </p>
            <Box display="flex" justifyContent='flex-end'>
                <Box flexGrow={1}> 
                  <Button variant='contained' onClick = {this.excluir} color='secondary' > Excluir </Button>
                </Box>
                <Box>
                <Button variant='contained' component={Link} to="/lista" color='primary' > Voltar Lista </Button>
                </Box>
            </Box>
        
            </Container>
      
          </>
        );
    

    }

}
