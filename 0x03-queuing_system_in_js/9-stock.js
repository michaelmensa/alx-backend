import { createClient, print } from 'redis';

import { promisify } from 'util';

const express = require('express');

const app = express();

const listProducts = [
  {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
  {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
  {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
  {id: 4, name: 'Suitcase 1050', price: 550, stock: 5},
];

function getItemById(id) {
  // function that gets item from listProducts by id
  const product = listProducts.find(item => item.id === id);
  return product;
}

app.get('/list_products', (req, res) =>{
  const response = listProducts.map(item => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock
  }));
  return res.json(response);
});

// create a client to connect to Redis Server
const client = createClient({
  url: 'redis://127.0.0.1:6380'
});

// promisify redis client methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function reserveStockById(itemId, stock) {
  // function will set in Redis the stock for the key item.ITEM_ID
  await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  // async func that returns the reserved stock for a specific item
  const reservedStock = await getAsync(`item.${itemId}`)
  return parseInt(reservedStock);
}

// get /list_products/:itemId return the current product and current stock
// available in JSON format
app.get('/list_products/:itemId', async (req, res) => {
  try {
    const itemId = parseInt(req.params.itemId);

    const product = getItemById(itemId);
    
    if (!product) {
      return res.status(404).json({ status: 'Product not found'});
    }

    // set reserve
    await reserveStockById(itemId, product.stock);
    const reservedStock = await getCurrentReservedStockById(itemId);
    // const currentQuantity = product.stock - reservedStock

    // construct a JSON response
    const response = {
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
      currentQuantity: reservedStock
    };

    return res.json(response);
  } catch (error) {
    console.log('Error', error);
    res.status(500).json({ error: 'Internal server error'});
  }
});

// express route to reserve a product by ID
app.get('/reserve_product/:itemId', async (req, res) => {
  try {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);

    if (!product) {
      return res.json({ status: 'Product not found'});
    }

    if (product.stock < 1) {
      return res.json({ status: 'Not enough stock available', itemId});
    }
    // reserve products
    const reservedStock = await getCurrentReservedStockById(itemId);
    await reserveStockById(itemId, reservedStock + 1);
    product.stock -= 1;

    return res.json({ status: 'Reservation confirmed', itemId});
  } catch (error) {
    console.log('Error', error);
  }
});

app.listen(1245);
