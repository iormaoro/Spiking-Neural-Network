#from parameters import param as par
#pixel_x = par.pixel_x

pixel_x = 8

print("if ( reset = '1' ) then")
print("     ram_address <= ( others => 'Z' );")
print("     ena <= '0';")
print("elsif ( clk'event and clk = '1' ) then")
print("     if ( prevneurons_spike(" +str(pixel_x*pixel_x-1)+ ")= '1' ) then")
print("         ram_address <= std_logic_vector(to_unsigned(" + str(0) +",10));")
print("         ena <= '1';")
for i in range(pixel_x*pixel_x - 1):
    print("     elsif ( prevneurons_spike(" +  str((pixel_x*pixel_x-1)-i-1) + ") = '1') then")
    print("         ram_Address <= std_logic_vector(to_unsigned(" + str(i+1) + ",10));")
    print("         ena <= '1';")
print("     else")
print("         ram_Address <= (others => 'Z');")
print("         ena <= '0';")
print("     end if;")
print("end if;")