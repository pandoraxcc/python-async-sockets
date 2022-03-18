## Why used TCP protocol for Python Sockets

Let's fist talk about TCP - Transmission Control Protocol allows us to communicate within the network and there are some advantages for a network application:</br> 

</br>Reliability: dropped packets on their way are detected and retransmitted to the endpoint</br>
Convenient way of reading data: all the packets sent arrive to the endpoint in the right order, meaning that the information is not mixed: if client sends "hello world", server recieves data as it is, but not "world hello".</br>
With that being said, TCP is great when we deal with applications that **require accurate information**, for example chats, emails</br></br>

Few words about UDP protocol (User Datagram Protocol) unlike TCP, UDP doesn't check if some pakcets were dropped on it's way; it can't re-send dropped packets to the client. That means that it's faster than TCP and that's one of the reason why it's mostly used in online games.
