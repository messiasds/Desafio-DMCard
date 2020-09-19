import React from 'react'
import {Link } from 'react-router-dom'

export default () => (
    <div>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/lista"> lista de cartão</Link>
          </li>
          <li>
            <Link to="/solicitar"> Solicitações de cartão</Link>
          </li>
        </ul>
      </nav>
    </div>
)
    