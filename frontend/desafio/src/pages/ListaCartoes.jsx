import React from 'react'
import Titulo from '../components/Titulo'
import Lista from '../components/Lista'
import {Button, Box, Container} from '@material-ui/core'
import {Link} from 'react-router-dom'
export default () =>  {

    return(    
      <>
      <Container maxWidth='sm'>
        <Titulo titulo = 'Pedidos de cartão realizados' />
        <Box display="flex" justifyContent='center' mb={2}>
          <Button size="large" variant='contained' color='primary' component={Link} to="/solicitar"> Solicitar cartão</Button>
        </Box>
        <Box display="flex" justifyContent='center' border={1} borderRadius={16} bgcolor="text.secondary" width="100%">
          <Lista />
        </Box>
      </Container>
      </>
)
    }