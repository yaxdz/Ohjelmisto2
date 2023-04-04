from flask import Flask, Response
import json
app = Flask(__name__)

@app.route('/summa/<luku1>/<luku2>')

const express = require('');
const { Sequelize, DataTypes } = require('sequelize');

const app = express();
const sequelize = new Sequelize('database', 'username', 'password', {
  dialect: 'sqlite',
  storage: 'database.sqlite'
});


const Airport = sequelize.define('Airport', {
  ICAO: {
    type: DataTypes.STRING,
    allowNull: false,
    primaryKey: true
  },
  Name: {
    type: DataTypes.STRING,
    allowNull: false
  },
  Municipality: {
    type: DataTypes.STRING,
    allowNull: false
  }
});


sequelize.sync();


app.get('/kenttä/:icao', async (req, res) => {
  const airport = await Airport.findOne({ where: { ICAO: req.params.icao } });
  if (!airport) {
    res.status(404).json({ error: 'Lentokenttää ei löytynyt' });
  } else {
    res.json({
      ICAO: airport.ICAO,
      Name: airport.Name,
      Municipality: airport.Municipality
    });
  }
});


app.listen(3000, () => {
  console.log('Sovellus käynnistetty osoitteessa http://localhost:3000');
});
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)