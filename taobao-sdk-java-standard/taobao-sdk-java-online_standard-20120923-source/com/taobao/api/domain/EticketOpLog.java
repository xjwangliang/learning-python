package com.taobao.api.domain;

import java.util.Date;

import com.taobao.api.TaobaoObject;
import com.taobao.api.internal.mapping.ApiField;

/**
 * 电子凭证操作记录
 *
 * @author auto create
 * @since 1.0, null
 */
public class EticketOpLog extends TaobaoObject {

	private static final long serialVersionUID = 8416289546552181692L;

	/**
	 * 操作金额
	 */
	@ApiField("amount")
	private String amount;

	/**
	 * 操作流水号
	 */
	@ApiField("consume_serial_num")
	private String consumeSerialNum;

	/**
	 * 操作数量
	 */
	@ApiField("num")
	private Long num;

	/**
	 * 操作时间
	 */
	@ApiField("op_time")
	private Date opTime;

	/**
	 * 操作类型 1:核销 2:冲正
	 */
	@ApiField("op_type")
	private Long opType;

	/**
	 * 订单ID
	 */
	@ApiField("order_id")
	private Long orderId;

	/**
	 * 操作员身份ID
	 */
	@ApiField("pos_id")
	private String posId;

	public String getAmount() {
		return this.amount;
	}
	public void setAmount(String amount) {
		this.amount = amount;
	}

	public String getConsumeSerialNum() {
		return this.consumeSerialNum;
	}
	public void setConsumeSerialNum(String consumeSerialNum) {
		this.consumeSerialNum = consumeSerialNum;
	}

	public Long getNum() {
		return this.num;
	}
	public void setNum(Long num) {
		this.num = num;
	}

	public Date getOpTime() {
		return this.opTime;
	}
	public void setOpTime(Date opTime) {
		this.opTime = opTime;
	}

	public Long getOpType() {
		return this.opType;
	}
	public void setOpType(Long opType) {
		this.opType = opType;
	}

	public Long getOrderId() {
		return this.orderId;
	}
	public void setOrderId(Long orderId) {
		this.orderId = orderId;
	}

	public String getPosId() {
		return this.posId;
	}
	public void setPosId(String posId) {
		this.posId = posId;
	}

}
