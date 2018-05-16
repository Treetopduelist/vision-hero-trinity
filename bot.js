const Discord = require('discord.js');
const client = new Discord.Client;

client.con('ready', ()=> {
    console.log('Bot is ready!')
});

client.on('message', message => {
    if (message.content === 'ping') {
        message.reply('pong!');
    }
});

client.login(process.env.NDIzMjU5MzQ2NzQ3NTIzMDc0.DdyNgQ.4x2dJBCvPFa7_m3K-Tw8survpD8);
