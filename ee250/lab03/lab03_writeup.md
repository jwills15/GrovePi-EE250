Joshua Williams
Lab 3

1. How did the reliability of UDP change when you added 50% loss to your local
environment? Why did this occur?
* The server became much less reliable because the server only displayed about 
50% of the client's inputs. For example, when the client input a sequence of
1-20, the server only displayed 2, 4, 5, 8, and 10. This occurred because UPD 
does not have built-in reliability. When 50% of the packets were lost during 
transmission, the UPD server had no way of knowing and it lost about 50% of the
client's inputs. 

2. How did the reliability of TCP change? Why did this occur?
* The reliability of the TCP connection did not change. When the client input
a sequence of 1-10, the server always displayed the full sequence of 1-10. This
occurred because TCP has built-in reliability. The TCP connection can recognize
when packets are lost through server/client communication, allowing for the lost
packets to be resent.

3. How did the speed of the TCP response change? Why might this happen?
* The speed of the TCP response was much slower when the packet loss was set to
50%. This is because the TCP connection recognized that packets were being lost
and waited until a lost packet was resent and correctly received before it was
displayed. TCP is also able to place received packets in the correct order, so
it waited for the next packet in the sequence to be received before displaying
even if it had already received a packet from later in the sequence.