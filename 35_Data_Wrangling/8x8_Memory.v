module memory (input clk,
               input reset,
               input op,
               input  [2:0] addr,
               input  [7:0] data_in,
               output reg [7:0] data_out);
  
  
  reg [7:0] memory_reg [8];
  
  always @ (negedge clk) begin
    
  if (reset) begin
      data_out <= 0;
    for (int i=0; i<8;i++) 
      memory_reg [i] <=0; 
  end
  else begin
    
  if (op) begin     // if op==1 then write data in memory 
      memory_reg [addr] <= data_in;
  end 
    
    
  else begin       // if op==0 read data from memory
    
    data_out <= memory_reg [addr];  
end
end
end
endmodule