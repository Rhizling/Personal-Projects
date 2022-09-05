const Discord = require("discord.js")
const client = new Discord.Client({ intents: [Discord.GatewayIntentBits.Guilds,Discord.GatewayIntentBits.GuildMessages] })

const minutes = 60, interval = minutes * 60 * 1000;

class Node {
  constructor(next, agendas, date) {
    this.next = next;
    this.agendas = agendas;
    this.date = date;
  } 
}

class DateList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  add(agendaNode) {
    if (head == null) {
      head, tail = new Node(null,agendaNode.agendas, agendaNode.date)    
    } else {
      if (tail == null) {
        head.next = agendaNode
        tail = agendaNode
      } else {
        tail.next = agendaNode
        tail = agendaNode
      }
    }
  }
  
  addOrder(agendaNode) {
    if (head == null) {
      head, tail = agendaNode
    } else {
      addOrderHelper(this, agendaNode, 2)
    }
  }

  addOrderHelper(list, agendaNode, dateIndex) {
    if (dateIndex < 0) {
      return
    }
    let newList = DateList()
    for (let i = list.head; i != null; i = i.next) {
      if (agendaNode.date[dateIndex] == i.date[dateIndex]) {
        newList.add(i)
      }
    }
    if (newList.head == null) {
      for (let curr = list.head; curr.next != null; curr = curr.next) {
        if (agendaNode.date[dateIndex] > curr.date[dateIndex] && agendaNode.next.date[dateIndex] > curr.next.date[dateIndex]) {
          agendaNode.next = curr.next
          curr.next = agendaNode
          return
        }
      }
      if (agendaNode.date[dateIndex] < head.date[dateIndex]){
        agendaNode.next = list.head
        list.head = agendaNode
      } else if (agendaNode.date[dateIndex] > tail.date[dateIndex]) {
        list.tail.next = agendaNode
        list.tail = agendaNode
      }
    } else if (newList.head.next == null && dateIndex == 0) {
      newList.head.agendas.append(agendaNode.agendas[0])
      return
    } else {
      addOrderHelper(newList, agendaNode, dateIndex-1)
    }
  }

  clear(dateToClear) {
    for (let i = this.head; i.next != null; i = i.next) {
      for (let j = i.date.length-1; j >= 0; j--) {
        if (i.next.date[j] != dateToClear[j]) {
          break
        } else if (j == 0) {
          i.next = i.next.next
          return true
        }
      }
    }
    return false
  }
}

const agenda_list = new DateList()

function date_to_string(date_list) {
  var date_string = ''
  for (let i = 0; i<3; i++) {
    if ((i == 0 || i == 1) && date_list[i] < 10) {
      date_string += '0'
    }
    date_string += toString(date_list[i])
    if (i != 3) {
      date_string += '/'
    }
  }
  return date_string
}

function string_to_date(date_string) {
  var date_list = [0,0,0]
  var counter = 0
      var curr_string = ""
      for (let i = 0; i < date_string.length(); i++) {
        curr_string += data_string.charAt(i)
        if (date_string.charAt(i) == "/") {
          date_list[counter++] = +curr_string
          curr_string = ""
        }
      }
      if (counter != 3) {
        msg.reply("Invalid Date Format")
        return null
      }
      return date_list
}
 
client.on("ready", () => {
  console.log("Ready")
})

client.on("messageCreate", msg => {
  if(msg.author.bot) return;
    if (msg.content.substring(0,4) == '!add') {
      var date = ""
      var date_reader = false
      for (let i = 4; i < msg.content.length(); i++) {
        if (msg.content.charAt(i) == " ") {
          if (date_reader == false) {
            date_reader = true
          } else {
            date += msg.content.charAt(i)
            var agenda = msg.content.substring(i+1,msg.content.length())
            break
          } 
        }
        if (date_reader) {
          date += msg.content.charAt(i)
        }
        if (date.length() > 10) {
          msg.reply("Invalid Date Format")
          return
        }
      }
      var date_list = string_to_date(date)
      if (date_list != null) { 
        agenda_list.addOrder(new Node(null,[agenda],date_list))
        msg.reply("Agenda Successfully Updated")
      }       
    } else if (msg.content.substring(0,6) == '!clear') {
      for (let i = 6; i < msg.content.length(); i++) {
          if (msg.content.charAt(i) == " ") {
              if (date_reader == false) {
                date_reader = true
              } else {
                date += msg.content.charAt(i)
                break
              } 
          }
          if (date_reader) {
              date += msg.content.charAt(i)
          }
          if (date.length() > 10) {
              msg.reply("Invalid Date Format")
              return
          }
        }
        var date_list = string_to_date(date)
        if (agenda_list.clear(date_list)) {
          msg.reply("Date has been cleared from agenda")
        } else {
          msg.reply("No such date exists in agenda")
        }
    } else if (msg.content.substring(0,5) == '!view') {
      for (let i = this.head; i.next != null; i = i.next) {
        var format = date_to_string(i.date).bold() + "\n"
        i.agendas.forEach((agenda) => {
          format += agenda + "\n"
        })
      }
      msg.reply(format)
    }   
  })

setInterval(function() {
  var today = new Date()
  var day = today.getDay()
  var month = today.getMonth();
  var year = today.getFullYear();
  var currentDate = [day,month,year]
  
  for (let i = agenda_list.head; i.next != null; i = i.next) {
    if (i.date == currentDate) {
      reminder = "Reminder: " + date_to_string(i.date) + "\n"
      for (agenda in i.agendas) {
        reminder += agenda + "\n"
      }
      msg.reply(reminder)
      agenda_list.clear(i.date)
      break
    }
  }
    
}, interval);
client.login('MTAwNjIxNTQ4OTQ4NTI5NTc4Ng.GYhsLn.mSer9v-RLnend6l3XbAjpJ_bPwoyxXwsiL7wtw')