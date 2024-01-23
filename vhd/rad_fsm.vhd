type MY_FSM_t is (RAD_WAIT_INIT, RAD_IDLE, RAD_PROCESSING, RAD_ERROR);
signal MY_FSM_STATE_s : MY_FSM_t;
signal MY_FSM_NEXT_STATE_s : MY_FSM_t;

p_MY_FSM_SYNCHRONOUS: process()
begin
   if () then
      MY_FSM_STATE_s <= ;
   elsif () then
      MY_FSM_NEXT_STATE_s <= ;
   end if;
end process;

p_MY_FSM_COMBINATIONAL: process()
begin
   case(MY_FSM_STATE_s) is
      when RAD_WAIT_INIT =>
         if (START_s = '1') then
            MY_FSM_NEXT_STATE_s <= RAD_IDLE;
         else
            MY_FSM_NEXT_STATE_s <= RAD_WAIT_INIT;
         end if;

      when RAD_IDLE =>
         if (INIT_s = '1') then
            MY_FSM_NEXT_STATE_s <= RAD_PROCESSING;
         else
            MY_FSM_NEXT_STATE_s <= RAD_IDLE;
         end if;

      when RAD_PROCESSING =>
         if (DONE_s = '1') then
            MY_FSM_NEXT_STATE_s <= RAD_IDLE;
         elsif (RAD_ERROR_s = '1') then
            MY_FSM_NEXT_STATE_s <= RAD_ERROR;
         else
            MY_FSM_NEXT_STATE_s <= RAD_PROCESSING;
         end if;

      when RAD_ERROR =>
         MY_FSM_NEXT_STATE_s <= RAD_IDLE;

      when others =>

   end case;
end process;

