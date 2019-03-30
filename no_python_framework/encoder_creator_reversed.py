#from parameters import param as par
#pixel_x = par.pixel_x

pixel_x = 28

# 0 rom

print("if ( reset = '1' ) then")
print("     ram_address_0 <= ( others => 'Z' );")
print("     ena_0 <= '0';")
print("elsif ( clk'event and clk = '1' ) then")
print("     if ( prevneurons_spike(" +str(3)+ ")= '1' ) then")
print("         ram_address_0 <= std_logic_vector(to_unsigned(" + str(195) +",8));")
print("         ena_0 <= '1';")
x=1
for i in xrange(6,pixel_x*pixel_x - 1,4):
    print("     elsif ( prevneurons_spike(" +  str(i+1) + ") = '1') then")
    print("         ram_Address_0 <= std_logic_vector(to_unsigned(" + str(195-x) + ",8));")
    print("         ena_0 <= '1';")
    x=x+1
print("     else")
print("         ram_Address_0 <= (others => 'Z');")
print("         ena_0 <= '0';")
print("     end if;")
print("end if;")

# 1 rom

print("if ( reset = '1' ) then")
print("     ram_address_1 <= ( others => 'Z' );")
print("     ena_1 <= '0';")
print("elsif ( clk'event and clk = '1' ) then")
print("     if ( prevneurons_spike(" +str(2)+ ")= '1' ) then")
print("         ram_address_1 <= std_logic_vector(to_unsigned(" + str(195) +",8));")
print("         ena_1 <= '1';")
x=1
for i in xrange(5,pixel_x*pixel_x - 1,4):
    print("     elsif ( prevneurons_spike(" +  str(i+1) + ") = '1') then")
    print("         ram_Address_1 <= std_logic_vector(to_unsigned(" + str(195-x) + ",8));")
    print("         ena_1 <= '1';")
    calcu=x+1
print("     else")
print("         ram_Address_1 <= (others => 'Z');")
print("         ena_1 <= '0';")
print("     end if;")
print("end if;")

# 2 rom

print("if ( reset = '1' ) then")
print("     ram_address_2 <= ( others => 'Z' );")
print("     ena_2 <= '0';")
print("elsif ( clk'event and clk = '1' ) then")
print("     if ( prevneurons_spike(" +str(1)+ ")= '1' ) then")
print("         ram_address_2 <= std_logic_vector(to_unsigned(" + str(195) +",8));")
print("         ena_2 <= '1';")
x=1
for i in xrange(4,pixel_x*pixel_x - 1,4):
    print("     elsif ( prevneurons_spike(" +  str(i+1) + ") = '1') then")
    print("         ram_Address_2 <= std_logic_vector(to_unsigned(" + str(195-x) + ",8));")
    print("         ena_2 <= '1';")
    x=x+1
print("     else")
print("         ram_Address_2 <= (others => 'Z');")
print("         ena_2 <= '0';")
print("     end if;")
print("end if;")

# 3 rom

print("if ( reset = '1' ) then")
print("     ram_address_3 <= ( others => 'Z' );")
print("     ena_3 <= '0';")
print("elsif ( clk'event and clk = '1' ) then")
print("     if ( prevneurons_spike(" +str(0)+ ")= '1' ) then")
print("         ram_address_3 <= std_logic_vector(to_unsigned(" + str(195) +",8));")
print("         ena_3 <= '1';")
x=1
for i in xrange(3,pixel_x*pixel_x - 1,4):
    print("     elsif ( prevneurons_spike(" +  str(i+1) + ") = '1') then")
    print("         ram_Address_3 <= std_logic_vector(to_unsigned(" + str(195-x) + ",8));")
    print("         ena_3 <= '1';")
    x=x+1
print("     else")
print("         ram_Address_3 <= (others => 'Z');")
print("         ena_3 <= '0';")
print("     end if;")
print("end if;")