type MY_FSM_t is (WAIT_INIT, IDLE, PROCESSING, ERROR, HANDLE_ERROR, NO_RESPONSE);
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
      when WAIT_INIT =>
         if (START_s = '1') then
            MY_FSM_NEXT_STATE_s <= IDLE;
         else
            MY_FSM_NEXT_STATE_s <= WAIT_INIT;
         end if;

      when IDLE =>
         if (INIT_s = '1') then
            MY_FSM_NEXT_STATE_s <= PROCESSING;
         else
            MY_FSM_NEXT_STATE_s <= IDLE;
         end if;

      when PROCESSING =>
         if (DONE_s = '1') then
            MY_FSM_NEXT_STATE_s <= IDLE;
         elsif (ERROR_s = '1') then
            MY_FSM_NEXT_STATE_s <= ERROR;
         else
            MY_FSM_NEXT_STATE_s <= PROCESSING;
         end if;

      when ERROR =>
         MY_FSM_NEXT_STATE_s <= HANDLE_ERROR;

      when HANDLE_ERROR =>
         if (ERROR) then
            MY_FSM_NEXT_STATE_s <= NO_RESPONSE;
         else
            MY_FSM_NEXT_STATE_s <= HANDLE_ERROR;
         end if;

      when NO_RESPONSE =>

      when others =>

   end case;
end process;

